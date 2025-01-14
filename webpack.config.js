const path = require('path');

module.exports = {
    entry: './index.js', // Your entry file that imports only what you need
    output: {
        filename: 'vtk-core-bundle.js', // Output bundle file
        path: path.resolve(__dirname, 'dist'),
        library: 'vtk', // This ensures vtk is exposed in the global scope
        libraryTarget: 'umd', // Universal module definition (works in most environments)
    },
    mode: 'production',
    optimization: {
        //usedExports: true, // Tree-shaking: only include used parts
        usedExports: false,
    },
};
