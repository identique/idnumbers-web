import { useState, FC } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

const App: FC = () => {
  const [country, setCountry] = useState<string | undefined>();
  const [idNumber, setIdNumber] = useState<string | undefined>();

  const handleSearch = () => {
    console.log(idNumber);
  };

  return (
    <div style={{ height: '100vh', display: 'flex', justifyContent: 'center' }}>
      <Box
        component="form"
        sx={{
          '& .MuiTextField-root': { width: '250px' },
        }}
        noValidate
        autoComplete="off"
        style={{ display: 'flex', alignItems: 'center', gap: '8px' }}
      >
        <FormControl style={{ minWidth: '100px' }}>
          <InputLabel id="country-select">Country</InputLabel>
          <Select labelId="country-select" id="country-select" label="Country">
            <MenuItem value={10}>USA</MenuItem>
            <MenuItem value={20}>TWN</MenuItem>
          </Select>
        </FormControl>
        <TextField
          id="country-id-number"
          value={idNumber}
          onChange={(e): void => setIdNumber(e.target.value)}
          placeholder="Identity number"
        />
        <Button variant="contained" onClick={handleSearch} size="large">
          Search
        </Button>
      </Box>
    </div>
  );
};

export default App;
