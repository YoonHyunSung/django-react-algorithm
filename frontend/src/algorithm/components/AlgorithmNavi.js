import React from "react"
import { Link } from "react-router-dom"

const AlgorithmNavi = () =>(
    <>
    <ul>
    <li><Link to='back-tracking' >BackTracking</Link></li>
    <li><Link to='brute-force' >BruteForce</Link></li>
    <li><Link to='divide-conquer' >DivideConquer</Link></li>
    <li><Link to='dynamic-conquer' >DynamicConquer</Link></li>
    <li><Link to='greedy' >Greedy</Link></li>
    </ul>
    </>
)
export default AlgorithmNavi