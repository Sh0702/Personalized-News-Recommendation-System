import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Signup from './pages/signup';
import Login from './pages/login';
import GenerateNews from './pages/generatenews';
import ProtectedRoute from './components/protectedroute';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route
          path="/generate"
          element={
            <ProtectedRoute>
              <GenerateNews />
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
