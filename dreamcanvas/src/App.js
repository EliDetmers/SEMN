import * as React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Home from './home';
import Configure from './configure_page';
import './App.css';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="/configure" element={<Configure />} />
        {/* <Route path="/Test" element={<Test />}/> */}
      </Routes>
    </Router>
  );
}
