const   express = require("express"),
        app = express(),
        bodyParser = require("body-parser"),
        expressSanitizer = require("express-sanitizer"),
        methodOverride = require("method-override"),
        mongoose = require("mongoose");

//APP CONFIG
//mongoose.connect("mongodb://localhost:27017/restful_blog_app", { useNewUrlParser: true });
app.set("view engine", "ejs");
app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended: true}));
app.use(expressSanitizer());
app.use(methodOverride("_method"));

// RESTful Routes

app.get("/", (req, res)=>{
    res.render("index");
})

app.get("/form", (req,res)=>{
    res.render("form")
})
app.get("/landingpage", (req,res)=>{
    res.render("landingpage")
})
app.get("/documentation", (req,res)=>{
    res.render("techdoc")
})
app.get("/tribute", (req,res)=>{
    res.render("tribute")
})

app.get("/todo", (req,res)=>{
    res.render("todo")
})

app.get("/colorGame", (req, res)=>{
    res.render("colorGame")
})

app.get("/memory", (req, res)=>{
    res.render("memory")
})

app.get("/businesscard", (req, res)=>{
    res.render("BChome")
})

app.get("/infracrete", (req, res)=>{
    res.render("infracrete")
})

app.get("/blog", (req, res)=>{
    res.render("blog")
})
/*
app.get("/businesscard/whoami", (req, res)=>{
    res.render("BCwhoami")
})
app.get("/businesscard/cv", (req, res)=>{
    res.render("BCcv")
})
app.get("/businesscard/contact", (req, res)=>{
    res.render("BCcontact")
})
app.get("/businesscard/offer", (req, res)=>{
    res.render("BCoffer")
})*/
app.get("/caesar", (req, res)=>{
    res.render("Caesars_cipher")
})
app.get("/roman", (req, res)=>{
    res.render("Roman_numeral_converter")
})
app.get("/palindrome", (req, res)=>{
    res.render("palindrome_checker")
})
app.get("/telephone", (req, res)=>{
    res.render("Telephone_Number_Validator")
})

// INDEX ROUTE
/*app.get("/blogs", (req,res)=>{
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
});*/

app.listen(3000, function(){
    console.log("Server is running!");
});