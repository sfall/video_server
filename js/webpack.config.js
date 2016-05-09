module.exports = {
    context: "js",
    entry: "./app/nav.js",
    output: {
        path: "./bundle.js"
    },
    resolve: {
        alias: {
            react: "./node_modules/react/react.js"
        },
        modulesDirectories: ["node_modules"]
    }
};