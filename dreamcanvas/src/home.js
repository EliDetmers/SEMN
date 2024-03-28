import * as React from 'react';
import { useNavigate } from 'react-router-dom';
import {Button} from '@mui/material';
import './App.css';


export default function Home() {
    const navigate = useNavigate();

    function handleCreate() {
        navigate("/configure");
    }

    return (
    <div className="App">
        <header className="App-header">
        <h1>Welcome to DreamScape</h1>
        <h4>Generative AI Model</h4>
        <Button variant="contained" onClick={handleCreate}>Begin Session</Button>
        <br />
        {/* <Button variant="contained">Load Previous Session</Button> */}
        </header>
    </div>
  );
}
