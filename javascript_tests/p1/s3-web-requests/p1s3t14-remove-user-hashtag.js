const FirebaseAuth = require('../../../includes/firebase_auth.js');
const configs = require('../../configs');
const querystring = require('querystring');
const axios = require('axios')

var firebase_auth = new FirebaseAuth();
var request_time = 0;
var request_url = "https://p1s3-web-requests-dot-aqueous-choir-160420.appspot.com/p1s3t14-remove-user-hashtag";

var params = {
    p1s3_firebase_email: configs.user_email,
    p1s3_token: '',
    p1s3t14_user_uid: '4813287573159936',
    p1s3t14_hashtag_uid: '5143213941719040'
};

var verify_token_success_callback = function(token) {
  params['p1s3_token'] = token;
  request_time = new Date().getTime();

  axios.post(request_url, querystring.stringify(params))
    .then(function (response) {
      let time_taken = new Date().getTime() - request_time;
      console.log(`Time took by request to complete is: ${time_taken/1000} seconds`);
      console.log(`Test passed: Response Success Code: ${response.status}`);
      console.log(`Test passed: Response Data: ${JSON.stringify(response.data)}`);
    })
    .catch(function (error) {
      let time_taken = new Date().getTime() - request_time;
      console.log(`Time took by request to complete is: ${time_taken/1000} seconds`);
      console.log(`There was an error while performing this operation. Error: ${error.response.status}`);
      console.log(`Test Failed: Response Data: ${JSON.stringify(error.response.data)}`);
    });
}

firebase_auth.loginUser(configs.user_email, configs.user_password, verify_token_success_callback)
