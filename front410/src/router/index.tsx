import LyricsSearchArea from '../components/lyricsSearchArea'
import SentimentSearchArea from '../components/sentimentSearchArea'
import Detail from '../components/songDetailPage'
import Home from '../views/home'
//import SongDetailPage from '../components/songDetailPage'
// Navigate 重定向组件
import {Navigate} from "react-router-dom"
import React,{ Children, lazy } from "react"
import Rec from '../components/recommendArea'

const withLoadingComponent = (comp:JSX.Element) => (
    <React.Suspense fallback={<div>Loading...</div>}>
        {comp}
    </React.Suspense>
)

const routes = [
    {
    path:"/", //重定向到home
    element:<Navigate to="/lyricsSearchArea" />,
    },
    {
        path:"/1/LSdetail",
        element: withLoadingComponent(<Detail />),
    },
    {
        path:"/",
        element: <Home />,
        children:[
            {
                path:"/recommendation",
                element: withLoadingComponent(<Rec />),
            },
            {
                path:"/lyricsSearchArea",
                element: withLoadingComponent(<LyricsSearchArea />),
                children:[
                    {
                        path:"/lyricsSearchArea/LSdetail",
                        element: withLoadingComponent(<Detail />),
                    }
                ]
            },
            {
                path:"/sentimentSearch",
                element: withLoadingComponent(<SentimentSearchArea />),
                children:[
                    {
                        path:"/sentimentSearch/LSdetail",
                        element: withLoadingComponent(<Detail />),
                    }
                ]
            },
            {
                path:"/LSdetail",
                element: withLoadingComponent(<Detail />),
            }
        ]
    }
    // {
    //     path:"/lyricsSearchArea",
    //     element:<LyricsSearchArea/>,
    // },
    // {
    //     path:"/home",
    //     element:<Home/>,
    //     },
    // {
    //     path:"/sentimentSearch",
    //     element:<SentimentSearchArea/>,
    // }
    // { path: "*", element: <Navigate to="/" /> },
]
export default routes