import { io } from "socket.io-client";
// import { SOCKET_URL } from "../../config";
import React from 'react';

export const SOCKET_URL = "http://localhost:5000";
export const socket = io(SOCKET_URL);
export const SocketContext = React.createContext(socket);
