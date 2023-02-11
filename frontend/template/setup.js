
import { readFileSync, writeFileSync } from 'fs';
import { resolve } from 'path';

const webPackConfigFile = resolve('./node_modules/react-scripts/config/webpack.config.js');
let webPackConfigFileText = readFileSync(webPackConfigFile, 'utf8');

if (!webPackConfigFileText.includes('watchOptions')) {
  if (webPackConfigFileText.includes('performance: false,')) {
    webPackConfigFileText = webPackConfigFileText.replace(
      'performance: false,',
      "performance: false,\n\t\twatchOptions: { aggregateTimeout: 200, poll: 1000, ignored: '**/node_modules', },"
    );
    writeFileSync(webPackConfigFile, webPackConfigFileText, 'utf8');
  } else {
    throw new Error(`Failed to inject watchOptions`);
  }
}