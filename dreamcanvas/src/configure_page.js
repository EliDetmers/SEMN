import * as React from 'react';
import { Grid, Button, TextField } from '@mui/material';
import AddCircleSharpIcon from '@mui/icons-material/AddCircleSharp';
import './App.css';

export default function Configure() {
  return (
    <div>
      <header className="Configuration-header">
        <Grid container spacing={2}>
          {/* Left Side */}
          <Grid item xs={8} className="left-side" style={{ marginTop: '1%' }}>    
            {/* <div className='Images-title'> */}
              Image:
            {/* </div> */}
          </Grid>

          {/* Right Side */}
          <Grid item xs={4} container direction="column" className='rightSide'>
            {/* Top part of the right side */}
            <Grid item className="top-right">
              <div>
                <div>
                  Add Image and Tag
                  </div>
                <AddCircleSharpIcon color='primary' sx={{ fontSize: 40}} />
              </div>
              <div>
                <Button variant="contained" style={{ display: 'flex-end', justifyContent: 'center'}}>Generate Model</Button>
              </div>
            </Grid>

            {/* Bottom part of the right side */}
            <Grid item className='bottom-right'>
              <TextField
                id="outlined-multiline-flexible"
                label="Enter your desired AI image render here:"
                multiline
                fullWidth
                rows={11.8}
                maxRows={10}
                className='AI-input-field'
              />
              <Button fullWidth variant="contained" style={{ display: 'flex-end', justifyContent: 'center'}}>Create Image</Button>
            </Grid>
          </Grid>
        </Grid>
      </header>
    </div>
  );
}
