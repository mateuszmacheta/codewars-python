# 4 kyu A Simplistic TCP Finite State Machine
# https://www.codewars.com/kata/54acc128329e634e9a000362/train/python

from enum import Enum


class State(Enum):
    CLOSED = 'CLOSED',
    LISTEN = 'LISTEN',
    SYN_SENT = 'SYN_SENT',
    SYN_RCVD = 'SYN_RCVD',
    ESTABLISHED = 'ESTABLISHED',
    CLOSE_WAIT = 'CLOSE_WAIT',
    LAST_ACK = 'LAST_ACK',
    FIN_WAIT_1 = 'FIN_WAIT_1',
    FIN_WAIT_2 = 'FIN_WAIT_2',
    CLOSING = 'CLOSING',
    TIME_WAIT = 'TIME_WAIT',
    ERROR = 'ERROR'


class Event(Enum):
    APP_PASSIVE_OPEN = 'APP_PASSIVE_OPEN',
    APP_ACTIVE_OPEN = 'APP_ACTIVE_OPEN',
    APP_SEND = 'APP_SEND',
    APP_CLOSE = 'APP_CLOSE',
    APP_TIMEOUT = 'APP_TIMEOUT',
    RCV_SYN = 'RCV_SYN',
    RCV_ACK = 'RCV_ACK',
    RCV_SYN_ACK = 'RCV_SYN_ACK',
    RCV_FIN = 'RCV_FIN',
    RCV_FIN_ACK = 'RCV_FIN_ACK'


fsm = {
    (State.CLOSED, Event.APP_PASSIVE_OPEN): State.LISTEN,
    (State.CLOSED, Event.APP_ACTIVE_OPEN): State.SYN_SENT,
    (State.LISTEN, Event.RCV_SYN): State.SYN_RCVD,
    (State.LISTEN, Event.APP_SEND): State.SYN_SENT,
    (State.LISTEN, Event.APP_CLOSE): State.CLOSED,
    (State.SYN_RCVD, Event.APP_CLOSE): State.FIN_WAIT_1,
    (State.SYN_RCVD, Event.RCV_ACK): State.ESTABLISHED,
    (State.SYN_SENT, Event.RCV_SYN): State.SYN_RCVD,
    (State.SYN_SENT, Event.RCV_SYN_ACK): State.ESTABLISHED,
    (State.SYN_SENT, Event.APP_CLOSE): State.CLOSED,
    (State.ESTABLISHED, Event.APP_CLOSE): State.FIN_WAIT_1,
    (State.ESTABLISHED, Event.RCV_FIN): State.CLOSE_WAIT,
    (State.FIN_WAIT_1, Event.RCV_FIN): State.CLOSING,
    (State.FIN_WAIT_1, Event.RCV_FIN_ACK): State.TIME_WAIT,
    (State.FIN_WAIT_1, Event.RCV_ACK): State.FIN_WAIT_2,
    (State.CLOSING, Event.RCV_ACK): State.TIME_WAIT,
    (State.FIN_WAIT_2, Event.RCV_FIN): State.TIME_WAIT,
    (State.TIME_WAIT, Event.APP_TIMEOUT): State.CLOSED,
    (State.CLOSE_WAIT, Event.APP_CLOSE): State.LAST_ACK,
    (State.LAST_ACK, Event.RCV_ACK): State.CLOSED,
}


def traverse_TCP_states(events):
    state = State.CLOSED
    for event in events:
        state = fsm.get((state, Event[event]), State.ERROR)
        if state == State.ERROR:
            return 'ERROR'
    return state.value[0]