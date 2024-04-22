const axios = require('axios');

axios
  .get('http://192.168.1.28:8000/hello', {
    todo: 'Buy the milk',
  })
  .then(res => {
    console.log(`statusCode : ${res.status}`);
    console.log(res);
  })
  .catch(error => {
    console.log(error);
  });

