import React, {useState} from 'react';
import InputForm from './InputForm';
import Timeline from './Timeline';
import './App.css';

const App = () => {
  const [item, setItem] = useState([[
    { type: 'string', id: 'Class' },
    { type: 'string', id: 'Detail' },
    { type: 'date', id: 'Start' },
    { type: 'date', id: 'End' },
  ]]);

  return (
    <div className='container'>
      <InputForm onSubmit={(input) => setItem([...item, input])} />
      <Timeline data={item}/>
    </div>
  );
}

export default App;
