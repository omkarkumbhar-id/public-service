FROM docker.io/node:lts-alpine

WORKDIR /app

RUN addgroup --system service-e2e && \
          adduser --system -G service-e2e service-e2e

COPY . service-e2e/
RUN chown -R service-e2e:service-e2e .

RUN npm --prefix service-e2e -f install

WORKDIR /app/service-e2e
CMD [ "npm", "run", "test:service" ]
