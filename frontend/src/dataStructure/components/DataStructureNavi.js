import React from "react"
import { Link } from "react-router-dom"

const DataStructureNavi = () =>(
    <>
    <ul>
    <li><Link to='linear' >Linear</Link></li>
    <li><Link to='math' >Math</Link></li>
    <li><Link to='non-linear' >NonLinear</Link></li>

    <li><Link to='quick-sort' >QuickSort</Link></li>
    <li><Link to='bubble-sort' >BubbleSort</Link></li>
    </ul>
    </>
)
export default DataStructureNavi