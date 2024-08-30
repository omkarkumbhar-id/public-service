import express from 'express';
import axios from 'axios';

const host = process.env.HOST ?? 'localhost';
const port = process.env.PORT ? Number(process.env.PORT) : 3000;

const app = express();

app.use(express.json());

app.get('/', (req, res) => {
  console.log("Received GET request on nxcontainer /")
  res.send({ message: 'Hello API GET' });
});

app.post('/', (req, res) => {
  console.log("Received GET request on nxcontainer /")
  res.send({ message: 'Hello API POST' });
});

app.get('/service', async (req, res) => {
  console.log("Received GET request on nxcontainer /service")
  try {
    const response = await axios.get('http://localhost:3001');
    res.status(response.status).send(response.data);
} catch (error) {
    console.error('Error fetching data from GET service:', error.message);
    res.status(500).send('An error occurred while fetching data from GET service.');
}
});

app.post('/service', async (req, res) => {
  console.log("Received GET request on nxcontainer /service")
  try {
    const response = await axios.post('http://localhost:3001');
    res.status(response.status).send(response.data);
} catch (error) {
    console.error('Error fetching data from POST service:', error.message);
    res.status(500).send('An error occurred while fetching data from POST service.');
}
});

app.listen(port, host, () => {
  console.log(`[ ready ] http://${host}:${port}`);
});
