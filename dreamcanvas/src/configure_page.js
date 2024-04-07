import React, { useState } from 'react';
import { Grid, Button, TextField } from '@mui/material';
import AddCircleSharpIcon from '@mui/icons-material/AddCircleSharp';
import Swal from 'sweetalert2';
import './App.css';

export default function Configure() {
  const [selectedZip, setSelectedZip] = useState(null);
  const [lora_url, set_lora_url] = useState(null);
  const [prompt, set_prompt] = useState("");
  const [image_url, set_image_url] = useState(null);

  const handleZipSelect = (event) => {
    const file = event.target.files[0];
    if (file) {
      // You can perform additional checks or operations here
      setSelectedZip(file);
    }
  };

  const handleLoraResponse = (response_url) => {
    if (response_url) {
      set_lora_url(response_url)
    }
    else {
      console.log("response was empty")
    }
  }

  const handleImageResponse = (image_url) => {
    if (image_url) {
      set_image_url(image_url)
    }
    else {
      console.log("image response was empty")
    }
  }

  const uploadAndTrainZip = async (zipFile) => {
    try {
      const formData = new FormData();
      formData.append('zip_file', zipFile);
  
      const loadingPopup = Swal.fire({
        title: 'Uploading and training...',
        allowOutsideClick: false,
        didOpen: () => {
          Swal.showLoading();
        }
      });
  
      const response = await fetch('http://localhost:5000/upload_and_train', {
        method: 'POST',
        body: formData
      });
  
      if (!response.ok) {
        throw new Error('Failed to upload and train zip file. Status: ' + response.status);
      }
  
      const data = await response.json();
      console.log('Training URL:', data.lora_url);
      handleLoraResponse(data.lora_url);
  
      loadingPopup.close();
  
      Swal.fire({
        icon: 'success',
        title: 'Training Successful!',
        text: `Training URL: ${data.lora_url}` // Assuming the returned JSON structure has a key 'lora_url'
      });
    } catch (error) {
      console.error('Error uploading and training zip file:', error.message);
  
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Failed to upload and train zip file.'
      });
    }
  };

  // Handler to update the prompt state whenever the TextField value changes
  const handlePromptChange = (event) => {
    set_prompt(event.target.value);
  };

  // Function to handle API call
  const createImage = async () => {
    try {

      const loadingPopup = Swal.fire({
        title: 'Creating your AI generated image...',
        allowOutsideClick: false,
        didOpen: () => {
          Swal.showLoading();
        }
      });
  
      const response = await fetch('http://localhost:5000/generate_image', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          prompt: prompt,
          lora_url: lora_url
        })
      });

      if (!response.ok) {
        throw new Error('Failed to generate image. Status: ' + response.status);
      }

      const data = await response.json();
      console.log('Generated Image URL:', data.output_url);

      handleImageResponse(data.output_url);

      loadingPopup.close();

    } catch (error) {
      console.error('Error generating image:', error.message);
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Failed to generate image.'
      });
    }
  };

  return (
    <div>
      <header className="Configuration-header">
        <Grid container spacing={2}>
          {/* Left Side */}
          <Grid item xs={8} className="left-side" style={{ marginTop: '1%' }}>
            <h2>Image</h2>
            <Grid item>
              {image_url && (
                <img src={image_url} alt="Generated Image" style={{ maxWidth: '100%', height: 'auto' }} />
              )}
            </Grid>
          </Grid>

          {/* Right Side */}
          <Grid item xs={4} container direction="column" className='rightSide'>
            {/* Top part of the right side */}
            <Grid item container direction="column" className="top-right" justifyContent="space-between">
              <Grid item>
                <div>
                  <div>
                    Add Images
                  </div>
                  <label htmlFor="zip-upload">
                    <AddCircleSharpIcon color='primary' sx={{ fontSize: 40 }} style={{ marginTop: '10px' }}/>
                    <input
                      id="zip-upload"
                      type="file"
                      accept=".zip"
                      style={{ display: 'none' }}
                      onChange={handleZipSelect}
                    />
                  </label>
                </div>
                {/* Display uploaded zip file */}
                {selectedZip && (
                  <Grid item className='uploaded-zip'>
                    <p>Uploaded Zip File: {selectedZip.name}</p>
                  </Grid>
                )}
              </Grid>
              {/* Empty grid item for spacing */}
              <Grid item></Grid>
              {/* Generate Model button */}
              <Grid item>
                <Button variant="contained" style={{ display: 'flex-end', justifyContent: 'center', marginBottom: '25%' }} onClick={() => uploadAndTrainZip(selectedZip)}>Generate Model</Button>
              </Grid>
            </Grid>

            {/* Bottom part of the right side */}
            <Grid item direction="column" className='bottom-right'>
              <TextField
                id="prompt"
                name="prompt"
                label="Enter your desired AI image render here:"
                multiline
                fullWidth
                rows={16.3}
                className='AI-input-field'
                value={prompt}
                onChange={handlePromptChange}
              />
              <Button fullWidth variant="contained" style={{ display: 'flex-end', justifyContent: 'center'}} onClick={createImage}>Create Image</Button>
            </Grid>
          </Grid>
        </Grid>
      </header>
    </div>
  );
}
