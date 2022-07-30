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

app.get("/blog", (req, res)=>{
    res.render("blog")
})

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

const PORT = process.env.PORT || 3000;

app.listen(PORT, function(){
    console.log(`Server is running! on port ${PORT}`);
});