// const FirebaseAuth = require('../../../includes/firebase_auth.js');
// const configs = require('../../configs');
const querystring = require('querystring');
const axios = require('axios')

// var firebase_auth = new FirebaseAuth();
var request_time = 0;
var request_url = "https://p1s3-web-requests-dot-aqueous-choir-160420.appspot.com/p1s3t4-modify-user-information";

////
// TODO - mu-Confirm format and Add missing params
////

var params = {
    // p1s3_firebase_email: configs.user_email,
    // p1s3_token: '',
    p1s3t4_user_uid: 'p1s2t1-04-081586330801_giver',
    p1s3t4_first_name: 'giver',
    p1s3t4_last_name: 'p1s2t1-04-08',
    p1s3t4_phone_number: "+62815111111",
    p1s3t4_phone_texts: "bbb",
    p1s3t4_phone_2: "+62815111112",
    p1s3t4_emergency_contact: "+62815111113",
    p1s3t4_home_address: "7371 Sherwood Street New York, NY 10032",
    p1s3t4_email_address: "example@mail.com",
    p1s3t4_firebase_uid: "0x8KZen30zWV6GWDH4ZP1czqapx2",
    p1s3t4_country_uid: "",
    p1s3t4_region_uid: "",
    p1s3t4_area_uid: "",
    p1s3t4_description: "New User Description",
    p1s3t4_preferred_radius: "5",
    p1s3t4_account_flags: "",
    p1s3t4_location_cord_long: "-73.935242",
    p1s3t4_location_cord_lat: "40.730610"
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
