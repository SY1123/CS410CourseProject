import styles from "./rec.module.scss"
import { Input, Space } from 'antd';
//import 'antd/dist/antd.css'; // or 'antd/dist/antd.less'
import { Divider } from 'antd';
import { Card } from 'antd';
import { ReactNode } from "react";
import React from "react";
import react from '@vitejs/plugin-react';
import { Link } from "react-router-dom";
import Title from "antd/lib/skeleton/Title";

const { Search } = Input;
class RecArea extends React.Component<{}, {searchResults: any[]},{item:any}> {
    constructor(props) {
        super(props);
        this.state = {
            //searchTerm: '', // 初始化状态，搜索关键词为空
            searchResults: [], // 初始化状态，搜索结果为空
        };
        fetch("http://127.0.0.1:5000/",{
            method:'GET',
            headers:{
                'Content-Type':'application/json;charset=UTF-8'
            },
            cache:'default'
        })
        .then(res => {
            return res.json()
        })
        .then(data => {
            console.log("dddd")
            console.log(data)
            //把数据赋值给 banners 然后渲染在页面上 
            this.setState({
                searchResults: data
            });
        })

      }

    // handleSearch(value : string){
    //     //在这里实现搜索逻辑，并将搜索结果更新到状态中
    //     const searchTerm = value
    //     //console.log("http://127.0.0.1:5000/sentiment_search?keyword="+searchTerm)
    //     fetch("http://127.0.0.1:5000/self_cosinesim?keyword="+searchTerm,{
    //         method:'GET',
    //         headers:{
    //             'Content-Type':'application/json;charset=UTF-8'
    //         },
    //         cache:'default'
    //     })
    //     .then(res => {
    //         return res.json()
    //     })
    //     .then(data => {
    //         console.log(data)
    //         //把数据赋值给 banners 然后渲染在页面上 
    //         this.setState({
    //             searchResults: data
    //         });
    //     })

    //     //console.log(searchTerm);
        
    // }


    render(): ReactNode {
        
        return(
            <div className={styles.lyricsSearchArea} style={{marginTop: 30}}>
                {/* <div className={styles.searchArea}>
                    <Search 
                    placeholder="Search the lyrics!" 
                    onSearch={value => this.handleSearch(value)} 
                    size = "large"
                    enterButton />
                 </div> */}
                <Divider plain>Recommendation</Divider>
                <div className={styles.resultArea}>
               <div>
                    {/* 对数组进行循环 */}
                    {
                        this.state.searchResults.map((value,key)=>{
                        //return<li  key={key}>{value.date}</li>
                        return(
                            <Card style={{width: 500, marginTop: 16}} title={value.title} extra={<Link to={`/LSdetail`} state={{value}} >More</Link> } >
                                <span>Artist: </span><span>{value.artist}</span>
                                <p><span>Release Date: </span><span>{value.release_date}</span></p>
                            </Card>
                            
                        )
                        })
                    }
                </div>
            </div>
                {/* <this.ResultArea></this.ResultArea> */}
            </div>
        )
    }
}

export default RecArea