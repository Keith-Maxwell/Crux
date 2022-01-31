import logo from './assets/CRUX_white.png';
import './App.css';
import { SocketContext, socket } from './context/socket';
import Game from './Game';

function App() {
  return (
    <SocketContext.Provider value={socket}>
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />

          <Game />
        </header>
      </div>
    </SocketContext.Provider>
  );
}

export default App;
