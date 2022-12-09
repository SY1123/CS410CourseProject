import { useState } from 'react'
import LyricsSearchArea from './components/lyricsSearchArea'
import SentimentSearchArea from './components/sentimentSearchArea'
import SongDetailPage from './components/songDetailPage'
import "./assets/styles/global.scss"
import router from './router';
import {useRoutes,Link} from "react-router-dom"


function App() {
  const [count, setCount] = useState(0)
  const outlet = useRoutes(router);

  return (
    <div className="App">
    {/* <Link to="/home">home</Link> |
    <Link to="/sentimentSearch">sentimentSearch</Link> */}

      {outlet}
    </div>
    )

  // return (
  //   <div className="App">
  //     <LyricsSearchArea></LyricsSearchArea>
  //     {/* <SentimentSearchArea></SentimentSearchArea> */}
  //     {/* <SongDetailPage></SongDetailPage> */}
  //   </div>
  // )
}

export default App
