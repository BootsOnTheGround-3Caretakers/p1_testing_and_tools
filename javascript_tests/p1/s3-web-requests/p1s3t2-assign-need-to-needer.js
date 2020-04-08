// const FirebaseAuth = require('../../../includes/firebase_auth.js');
// const configs = require('../../configs');
const querystring = require('querystring');
const axios = require('axios')

// var firebase_auth = new FirebaseAuth();
var request_time = 0;
var request_url = "https://p1s3-web-requests-dot-aqueous-choir-160420.appspot.com/p1s3t2-assign-need-to-needer";

var params = {
    // p1s3_firebase_email: configs.user_email,
    // p1s3_token: '',
    p1s3t2_need_uid: '5632908932939776',
    p1s3t2_needer_uid: '5716776893546496',
    p1s3t2_user_uid: 'p1s2t1-04-081586331875_needer',
    p1s3t2_special_requests: 'Be precise on the dose.',
};

var verify_token_success_callback = function(token) {
  // params['p1s3_token'] = token;
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

// Making request directly without firebase authentication
verify_token_success_callback("");

// firebase_auth.loginUser(configs.user_email, configs.user_password, verify_token_success_callback)
