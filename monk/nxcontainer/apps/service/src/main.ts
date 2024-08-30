import express from 'express';

const host = process.env.HOST ?? 'localhost';
const port = process.env.PORT ? Number(process.env.PORT) : 3001;

const app = express();

app.use(express.json());

app.get('/', (req, res) => {
  res.send({ message: 'Hello API GET from service' });
});

app.post('/', (req, res) => {
  res.send({ message: 'Hello API POST from service' });
});

app.listen(port, host, () => {
  console.log(`[ ready ] http://${host}:${port}`);
});
