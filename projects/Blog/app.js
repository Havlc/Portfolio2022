const express = require("express"),
app = express(),
bodyParser = require("body-parser"),
expressSanitizer = require("express-sanitizer"),
methodOverride = require("method-override"),
mongoose = require("mongoose");

// configure dotenv
require('dotenv').config();
//APP CONFIG
mongoose.connect(process.env.MONGODB_URI, {
        useNewUrlParser: true,
        useCreateIndex: true
}).then(() => {
    console.log("Connected to DB!");
}).catch(err => {
    console.log("ERROR", err.message);
});


mongoose.set('useNewUrlParser', true);
mongoose.set('useFindAndModify', false);
mongoose.set('useCreateIndex', true);
app.set("view engine", "ejs");
app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended: true}));
app.use(expressSanitizer());
app.use(methodOverride("_method"));
mongoose.set('useFindAndModify', false);

//MONGOOSE/MODEL CONFIG
const blogSchema = new mongoose.Schema({
        title: String,
        image: String,
        body: String,
        created: {type: Date, default: Date.now}
});

const Blog = mongoose.model("Blog", blogSchema);

// RESTful Routes

app.get("/", (req, res)=>{
    res.redirect("blogs");
})

// INDEX ROUTE
app.get("/blogs", (req,res)=>{
    Blog.find({}, (err, blogs)=>{
        if(err){
            console.log("ERROR!");
        } else{
            res.render("index", {blogs: blogs});
        }
    });
});

// NEW ROUTE
app.get("/blogs/new", (req,res)=>{
    res.render("new");
});

// CREATE ROUTE
app.post("/blogs",(req,res)=>{
    //create blog
    console.log(req.body);
    req.body.blog.body = req.sanitize(req.body.blog.body)
    console.log("=========");
    console.log(req.body);
    Blog.create(req.body.blog, (err, newBlog)=>{
        if (err){
            res.render("new");
        }else{
            // than redirect to the index
            res.redirect("blogs");
        }
    });

});

// SHOW ROUTE
app.get("/blogs/:id", (req, res)=>{
        Blog.findById(req.params.id, (err, foundBlog)=>{
            if (err){
                res.redirect("/blogs");
            } else{
                res.render("show", {blog: foundBlog})
            }
        });
    });

// EDIT ROUTE
app.get("/blogs/:id/edit", (req,res)=>{
    Blog.findById(req.params.id, (err, foundBlog)=>{
        if (err){
            res.redirect("/blogs");
        } else {
            res.render("edit", {blog: foundBlog});
        }
    });
});

// UPDATE ROUTE
app.put("/blogs/:id/", (req, res)=>{
    req.body.blog.body = req.sanitize(req.body.blog.body)
   Blog.findByIdAndUpdate(req.params.id, req.body.blog, (err, updatedBlog)=>{
       if (err){
           res.redirect("/blogs");
       } else {
           res.redirect("/blogs/"+req.params.id);
       }
   });
});
// DELETE ROUTE
app.delete("/blogs/:id", (req, res)=>{
    //destroy blog
    Blog.findByIdAndRemove(req.params.id, (err)=>{
        if(err){
            res.redirect("/blogs");
        } else {
            res.redirect("/blogs");
        }
    });
    // redirect
});
//const PORT = process.env.PORT || 3000;
app.listen(process.env.PORT, function(){
    console.log("Server is running!");
});