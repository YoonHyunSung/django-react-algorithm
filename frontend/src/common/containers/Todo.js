import React from "react"
import {TodoList, TodoInput} from 'common/index'
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