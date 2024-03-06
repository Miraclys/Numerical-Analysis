# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

#### 数学公式

$$
\sum
$$

$\int$

#### Code

```
const express = require('express');
const multer = require('multer');
const serveIndex = require('serve-index');
const path = require('path');
const fs = require('fs');

const app = express();
const port = 3000;

// Set the directory for file uploads
const uploadDirectory = path.join(__dirname, 'uploads');
fs.mkdirSync(uploadDirectory, { recursive: true });

// Configure multer for file uploads
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, uploadDirectory); // 指定文件存储位置
    },
    filename: function (req, file, cb) {
      // 使用原始文件名，并确保以UTF-8编码保存
      cb(null, Buffer.from(file.originalname, 'latin1').toString('utf8'));
    }
});  

const upload = multer({ storage: storage });

// Serve the HTML file for uploading files
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Route for file uploads
// app.post('/upload', upload.single('file'), (req, res) => {
//   res.json({ message: 'File uploaded successfully' }); // Respond with JSON
// });

app.post('/upload', upload.single('file'), (req, res) => {
    const originalName = req.file.originalname;
    // 对原始文件名进行处理，例如URL编码
    const encodedName = encodeURIComponent(originalName);
    
    // 将文件重命名为经过处理的名称
    fs.renameSync(req.file.path, path.join(uploadDirectory, encodedName));
  
    res.json({ message: '文件上传成功' });
});
  
// app.post('/upload', upload.single('file'), (req, res) => {
//     let filename = decodeURIComponent(req.file.originalname); // Decode URI component
//     // Rename the file to the decoded filename
//     fs.renameSync(req.file.path, path.join(uploadDirectory, filename));
    
//     res.json({ message: '文件上传成功' });
// });


// Serve files and enable directory listing
app.use('/files', express.static(uploadDirectory), serveIndex(uploadDirectory, { 'icons': true }));

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
```