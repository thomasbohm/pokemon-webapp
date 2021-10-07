import axios from 'axios';
import { useState } from 'react';

export default function App() {
  const [imgFile, setImgFile] = useState();
  
  function onFileChange(event) {
    console.log(event.target.files[0]);
    setImgFile(event.target.files[0])
  }

  async function onFileUpload() {
    if (!imgFile) {
      return;
    }
    
    const formData = new FormData();
    formData.append(
      "file",
      imgFile,
      imgFile.name
    );

    try {
      const res = await axios.post("http://127.0.0.1:5000/", formData);
      console.log(res.data);
    } catch (e) {
      console.log('Error: ' + e);
    }
  }

  return (
    <div>
        <h1>
          Pokemon Classifier
        </h1>
        <h3>
          Upload your image
        </h3>
        <div>
          <input type="file" onChange={onFileChange} />
          <button onClick={onFileUpload}>Upload</button>
        </div>
    </div>
  );
}
