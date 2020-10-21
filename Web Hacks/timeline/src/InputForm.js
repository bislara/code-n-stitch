import React, {useState } from 'react';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

const InputForm = (props) => {
  const [cat, setCat] = useState('');
  const [detail, setDetail] = useState('');
  const [start, setStart] = useState(new Date());
  const [end, setEnd] = useState(new Date());

  /* Returns the input to the parent */
  const handleSubmit = (e) => {
    e.preventDefault();
    if (cat === '' || detail === '' || end <= start) return;
    props.onSubmit([cat, detail, start, end]);
    clearInput();
  }

  /* Resets the inputs */
  const clearInput = () => {
    setCat('');
    setDetail('');
    setStart(new Date());
    setEnd(new Date());
  }

  return (
    <form className='row mt-5' onSubmit={(e) => handleSubmit(e)}>
      <div className='col-6'>
        <input type='text' className='form-control mb-3' placeholder='Enter Category' value={cat} 
          onChange={(e) => setCat(e.target.value)} 
        />
        <input type='text' className='form-control mb-3' placeholder='Enter Detail' value={detail} 
          onChange={(e) => setDetail(e.target.value)} 
        />
      </div>
      <div className='col-4'>
        <DatePicker selected={start} onChange={date => setStart(date)} showTimeSelect dateFormat="Pp"/>
        <DatePicker selected={end} onChange={date => setEnd(date)} showTimeSelect dateFormat="Pp"/>
      </div>
      <div className='col-2'>
        <button type='submit' className='btn btn-block btn-primary mb-3'>Add Item</button>
        <button type='button' className='btn btn-block btn-secondary' onClick={() => clearInput()}>Clear</button>
      </div>
    </form>
  )
}

export default InputForm;