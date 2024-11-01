# docker run -p 3001:3001 --name experiment-service -d experiment-service

FROM node:lts-alpine

ENV HOST=0.0.0.0
ENV PORT=3001

WORKDIR /app

RUN addgroup --system service && \
          adduser --system -G service service

COPY dist/apps/service service/
RUN chown -R service:service .

RUN npm --prefix service --omit=dev -f install

CMD [ "node", "service" ]
