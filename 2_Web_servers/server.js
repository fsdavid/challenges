const express = require('express');
const router = require('./routes')

const app = express();

// Use base routes
app.use(`/${process.env.BASE_URL}`, router);

// Start server
app.listen(process.env.PORT);
