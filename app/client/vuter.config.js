// vetur.config.js
/** @type {import('vls').VeturConfig} */
module.exports = {
  settings: {
    "vuter.experimental.templateInterpolationService": true,
  },
  projects: [
    {
      root: "./",
      package: "./package.json",
      globalComponents: ["./src/components/**/*.vue", "./src/views/**/*.vue"],
      tsconfig: "./tsconfig.json",
    },
  ],
};
