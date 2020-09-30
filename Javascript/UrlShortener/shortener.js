/*
    If you want to test this out 
    1. npm install
    2. get your Access_token
    3. run by using node
*/

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
/* Bitly Usage
const { BitlyClient} = require('bitly');
const ACCESS_TOKEN = "YOUR ACCESS TOKEN HERE"
const bitly = new BitlyClient(ACCESS_TOKEN, {});


readline.question("Enter your URI: ",async (uri) =>{
    try{
        let result = await bitly.shorten(uri)
        console.log( result.link)
    }catch(e){
        throw e;
    }finally{
        readline.close()
    }
})
*/
// for more information: https://www.npmjs.com/package/bitly

const TinyURL = require("tinyurl");
readline.question("Enter your URI: ", async (uri) => {
  TinyURL.shorten(uri, function (response, error) {
    if (error) throw error;
    console.log(response);
  });
});
