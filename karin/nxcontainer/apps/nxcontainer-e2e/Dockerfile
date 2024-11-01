FROM node:lts-alpine

WORKDIR /app

RUN addgroup --system nxcontainer-e2e && \
          adduser --system -G nxcontainer-e2e nxcontainer-e2e

COPY . nxcontainer-e2e/
RUN chown -R nxcontainer-e2e:nxcontainer-e2e .

RUN npm --prefix nxcontainer-e2e -f install

WORKDIR /app/nxcontainer-e2e
CMD [ "npm", "run", "test:nxcontainer" ]
