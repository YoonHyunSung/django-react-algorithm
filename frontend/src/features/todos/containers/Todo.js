import React from "react"
import {TodoList, TodoInput} from 'features/todos'
import styled from 'styled-components'
export default function Todo() {
    return(
        <CounterDiv>
            <TodoInput/>
            <TodoList/>
        </CounterDiv>
    )
    
}

const CounterDiv = styled.div`text-align: center;`