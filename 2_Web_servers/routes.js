const express = require('express')
const router = express.Router()

router.get('/foo', function (req, res) { 
    res.json({
        response: 'Hello'
    })
})

router.get('/bar', function (req, res) { 
    res.json({
        response: 'World'
    })
})

module.exports = router