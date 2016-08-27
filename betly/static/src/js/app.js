/**
 * Main application initialization
 *
 */

import React from 'react'
import ReactDOM from 'react-dom'

import TestComponent from './example/test.jsx'

// Initialize on Document Ready
document.addEventListener('DOMContentLoaded', () => {
  var main = document.getElementById('main')
  ReactDOM.render(<TestComponent />, main)
})
