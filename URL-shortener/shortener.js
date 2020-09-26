const { BitlyClient} = require('bitly');
const bitly = new BitlyClient('9f7e4b81998f4bea73b3999cdc166ee97d600bc7', {});

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
})

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