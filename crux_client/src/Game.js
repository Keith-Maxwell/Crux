import React, { useState, useContext, useCallback, useEffect } from 'react';
import { SocketContext } from './context/socket';

function Button(props) {
    return (
        <button className="button" onClick={props.onClick}>
            {props.text}
        </button>
    );
}


function Game(props) {
    const socket = useContext(SocketContext);
    let [counter, setCounter] = useState(0);

    const handleClick = useCallback(() => {
        console.log('click');
        socket.emit("ask-for-counter-update");
    }, []);

    useEffect(() => {
        socket.on("update-counter", (data) => {
            console.log(data);
            setCounter(data.counter);
        });
    });
    return (
        <div className="game">
            <Button text="Click me!" onClick={handleClick} />
            <div className="game-info">
                <div>{counter}</div>
                <ol>{/* TODO */}</ol>
            </div>
        </div>
    );

}

// ========================================

export default Game;
