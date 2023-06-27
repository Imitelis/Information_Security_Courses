const express = require('express');

const app = express();

// #1 - Install and Require Helmet
const helmet = require('helmet');

// #2 - Hide Potentially Dangerous Information Using helmet.hidePoweredBy()
app.use(helmet.hidePoweredBy());

// #3 - Mitigate the Risk of Clickjacking with helmet.frameguard()
app.use(helmet.frameguard({ action: 'deny' }));

// #4 - Mitigate the Risk of Cross Site Scripting (XSS) Attacks with helmet.xssFilter()
app.use(helmet.xssFilter());

// #5 - Avoid Inferring the Response MIME Type with helmet.noSniff()
app.use(helmet.noSniff());

// #6 - Prevent IE from Opening Untrusted HTML with helmet.ieNoOpen()
app.use(helmet.ieNoOpen());

// #7 - Ask Browsers to Access Your Site via HTTPS Only with helmet.hsts()
const ninetyDaysInSeconds = 90 * 24 * 60 * 60;

app.use(helmet.hsts({ maxAge: ninetyDaysInSeconds, force: true }));

// #8 - Disable DNS Prefetching with helmet.dnsPrefetchControl()
app.use(helmet.dnsPrefetchControl());

// #9 - Disable Client-Side Caching with helmet.noCache()
app.use(helmet.noCache());

// #10 - Set a Content Security Policy with helmet.contentSecurityPolicy()
app.use(helmet.contentSecurityPolicy({ directives: { defaultSrc: ["'self'"], scriptSrc: ["'self'", "trusted-cdn.com"] } }));

// #11 - Configure Helmet Using the ‘parent’ helmet() Middleware
app.use(helmet({
  frameguard: {         // configure
    action: 'deny'
  },
  contentSecurityPolicy: {    // enable and configure
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ['style.com'],
    }
  },
  dnsPrefetchControl: false     // disable
}));

module.exports = app;
const api = require('./server.js');
app.use(express.static('public'));
app.disable('strict-transport-security');
app.use('/_api', api);
app.get("/", function(request, response) {
  response.sendFile(__dirname + '/views/index.html');
});
let port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Your app is listening on port ${port}`);
});
