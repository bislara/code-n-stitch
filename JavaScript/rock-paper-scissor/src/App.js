import { useState } from 'react';
import './App.css';
import JSConfetti from 'js-confetti'
<style>
@import url('https://fonts.googleapis.com/css2?family=Italianno&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap');
</style>
const image = {
  Rock : "https://i.imgur.com/TONXH9s.png",
  Paper :"https://i.imgur.com/t2154qR.png",
  Scissor:"https://i.imgur.com/SXstPKk.png}"
}

const jsConfetti = new JSConfetti()
function App() {
  const[Name,setName] = useState('');
  const [userChoice,setuserChoice]=useState(null);
  const [compChoice,setcompChoice]=useState(null);
  const[isStarted,setisStarted] = useState(false);
  let userScore =0;
  let compScore = 0;

const handleClick = () =>{
  
  setisStarted(true);
}
// const keys = Object.keys(image)
// const prop = keys[Math.floor(Math.random() * keys.length)]
// setcompChoice(prop);
const selectWinner = (user,comp) =>{
  if(user===comp){
      return "Tie";
  }else if((user ==="Paper" && comp ==="Rock") || (user==="Scissor" && comp==="Paper") || (user==="Rock" && comp==="Scissor")){
      return user;
  }else{
      return comp;
  }

}





const handleChange = (event) =>{
   setName(event.target.value);
   
}
console.log(userChoice);

console.log(compChoice);

console.log(Name);
  return (
    isStarted ? (<div >
    <div  className="choose">
    
    {userChoice ?<div  > <h1>{Name} choose </h1> <img className="user-img" alt="lll" src={image[userChoice]}></img> </div>  :(<div>
        <h1>{Name} Select you choice</h1>
        
      {Object.keys(image).map((a) =>{
        return(<div    key={a}> <span  onClick = {() => {setuserChoice(a);
      setcompChoice(Object.keys(image)[Math.floor(Math.random() * Object.keys(image).length)])  } }> <img  className="random-image" alt=""src={image[a]}></img>  </span>
                     </div>
      )})}
        </div>)}
        
        <div>
            <h1 className="comp">Computer {compChoice ? "choose" : ""}</h1>
     <div className="comp"><img alt= "all" className={userChoice ? "comp" : "comp-img"} src={compChoice ? image[compChoice] : "https://i.imgur.com/CyvHqQH.png"}></img> </div> 
            
        </div>
         
        </div>

        <div>{ userChoice && compChoice && (<div className="result"> <p> {(() => {
              const Winner = selectWinner(userChoice, compChoice);
              if (Winner === "Tie") {
                return "Match tied!";
              } else {
                if (Winner === userChoice) {
                  userScore=userScore+1;
                  jsConfetti.addConfetti()
                  return Name + " Wins!";

                  
                } else {
                  compScore=compScore+1;
                  return "Computer Wins!";
                 
                }
              }
            })()}</p> <p>Your score is : {userScore}</p> <p>Computer score is : {compScore}</p>
            <button className="restart-button" onClick = {() => {
             setuserChoice(null); setcompChoice(null); setisStarted(false)}}>Restart</button>
            </div>)}</div>

   

        
    </div>) :
    (<div className="App">
     <h1>Rock Paper Scissor</h1>
     
     <form> 
      <h3>Enter Player Name</h3>
      <input className="input"type="text" onChange = {handleChange}></input><br />
      <button onClick={handleClick} className="play-button"> Lets play </button>
      </form>
      <img alt="minions" className="minions" src="data:image/png;base64,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"></img>

    </div>)
  );
}

export default App;
