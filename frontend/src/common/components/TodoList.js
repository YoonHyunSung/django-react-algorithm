import React from "react"
import {useDispatch, useSelector} from 'react-redux'
const TodoList = ()=>{
    const todos = useSelector(state => state.todos)
    
    return(<>
        {todos.length === 0 && (<h1>등록된 목록이없습니다.</h1>)}
        {todos.length !== 0 && (<h1>{todos.length} 개의 할일 목록이 있습니다.</h1>)}
        </>
    )
}
export default TodoList