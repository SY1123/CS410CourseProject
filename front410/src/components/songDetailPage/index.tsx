import styles from "./songDetail.module.scss"
import { Descriptions } from 'antd';
// import 'mac-scrollbar/dist/mac-scrollbar.css';
// import { MacScrollbar } from 'mac-scrollbar';
import { Divider } from 'antd';
import { Scrollbars } from 'react-custom-scrollbars-2';
import React from "react";
// import qs from 'querystring'
import { useParams, useLocation, Link } from 'react-router-dom';


// class SongDetailPage extends React.Component{
//     constructor(props) {
//         super(props);
    
//         this.state = {
//           item: {
//             // item 的值
//           }
//         };
//       }

//     render() {
//         console.log(window.location)
//         // const params = useParams();
//         // console.log(params)
//         return(
//             <div className={styles.songDetail}>
//                 <div className={styles.basic}>
//                     <Descriptions title="Song Info">
//                     <Descriptions.Item label="Artist">Lady Gaga</Descriptions.Item>
//                     <Descriptions.Item label="Album">XXXXX</Descriptions.Item>
//                     <Descriptions.Item label="Released">Oct. 22, 2012</Descriptions.Item>
//                     <Descriptions.Item label="Genre">Pop, soft rock</Descriptions.Item>
//                     </Descriptions>
//                 </div> 
//                 <Divider  plain>Lyrics</Divider>

//                 <div className={styles.lyrics}>
//                     <Scrollbars style={{width: 500, height: 300 }}>
//                         <p>I wanna hold 'em like they do in Texas, please <br />
//                             Fold 'em, let 'em hit me, raise it, baby, stay with me (I love it)<br />
//                             Love game intuition, play the cards with spades to start<br />
//                             And after he's been hooked, I'll play the one that's on his heart<br />
//                             Oh, whoa, oh, oh<br />
//                             Oh, oh-oh<br />
//                             I'll get him hot, show him what I got<br />
//                             Oh, whoa, oh, oh<br />
//                             Oh, oh-oh<br />
//                             I'll get him hot, show him what I got<br />
//                             Can't read my, can't read my<br />
//                             No, he can't read my poker face<br />
//                             (She's got me like nobody)<br />
//                             Can't read my, can't read my<br />
//                             No, he can't read my poker face<br />
//                             (She's got me like nobody)<br />
//                             P-p-p-poker face, f-f-fuck her face (mum-mum-mum-mah)<br />
//                             P-p-p-poker face, f-f-fuck her face (mum-mum-mum-mah)<br />
//                             Fold 'em, let 'em hit me, raise it, baby, stay with me (I love it)<br />
//                             Love game intuition, play the cards with spades to start<br />
//                             And after he's been hooked, I'll play the one that's on his heart<br />
//                             Oh, whoa, oh, oh<br />
//                             Oh, oh-oh<br />
//                             I'll get him hot, show him what I got<br />
//                             Oh, whoa, oh, oh<br />
//                             Oh, oh-oh<br />
//                             I'll get him hot, show him what I got<br />
//                             Can't read my, can't read my<br />
//                         </p>
//                     </Scrollbars>
//                 </div> 
//             </div>
//         )
//     }
   
// }

// export default SongDetailPage

// function Lyrics(){
//     return(
//         <div className={styles.lyrics}>
//             <Scrollbars style={{width: 500, height: 300 }}>
//                 <p>I wanna hold 'em like they do in Texas, please <br />
//                     Fold 'em, let 'em hit me, raise it, baby, stay with me (I love it)<br />
//                     Love game intuition, play the cards with spades to start<br />
//                     And after he's been hooked, I'll play the one that's on his heart<br />
//                     Oh, whoa, oh, oh<br />
//                     Oh, oh-oh<br />
//                     I'll get him hot, show him what I got<br />
//                     Oh, whoa, oh, oh<br />
//                     Oh, oh-oh<br />
//                     I'll get him hot, show him what I got<br />
//                     Can't read my, can't read my<br />
//                     No, he can't read my poker face<br />
//                     (She's got me like nobody)<br />
//                     Can't read my, can't read my<br />
//                     No, he can't read my poker face<br />
//                     (She's got me like nobody)<br />
//                     P-p-p-poker face, f-f-fuck her face (mum-mum-mum-mah)<br />
//                     P-p-p-poker face, f-f-fuck her face (mum-mum-mum-mah)<br />
//                     Fold 'em, let 'em hit me, raise it, baby, stay with me (I love it)<br />
//                     Love game intuition, play the cards with spades to start<br />
//                     And after he's been hooked, I'll play the one that's on his heart<br />
//                     Oh, whoa, oh, oh<br />
//                     Oh, oh-oh<br />
//                     I'll get him hot, show him what I got<br />
//                     Oh, whoa, oh, oh<br />
//                     Oh, oh-oh<br />
//                     I'll get him hot, show him what I got<br />
//                     Can't read my, can't read my<br />
//                 </p>
//             </Scrollbars>
//         </div>    
//     )
// }



function BasicInformation(){
    return(
        <div className={styles.basic}>
            <Descriptions title="Song Info">
            <Descriptions.Item label="Artist">Lady Gaga</Descriptions.Item>
            <Descriptions.Item label="Album">XXXXX</Descriptions.Item>
            <Descriptions.Item label="Released">Oct. 22, 2012</Descriptions.Item>
            <Descriptions.Item label="Genre">Pop, soft rock</Descriptions.Item>
            
        </Descriptions>
        </div>       
    )
}

function SongDetailPage(){
    //console.log(useParams())
    //console.log(qs.parse(useLocation().search))
    console.log(useLocation().state.value)
    const value = useLocation().state.value
    const msg = new String(value.lyric);
    let arr = msg.split('.');

    return(
        <div className={styles.songDetail}>
            <div className={styles.basic}>
                <Descriptions title="Song Info">
                <Descriptions.Item style={{fontWeight: 550}} label="Artist">{value.artist==null? "n/a" : value.artist}</Descriptions.Item>
                <Descriptions.Item style={{fontWeight: 550}} label="">{}</Descriptions.Item>
                <Descriptions.Item style={{fontWeight: 550}} label="Released">{value.release_date}</Descriptions.Item>
                
                <Descriptions.Item style={{fontWeight: 550}} label="Genre">{value.genre}</Descriptions.Item>
                
                </Descriptions>
            </div> 
            <div style={{marginTop: 40 }}>
              <a href={value.spotify_link}>Listen on Spotify</a>
            </div>
            <Divider  plain>Lyrics</Divider>
            <div className={styles.lyrics}>
                <Scrollbars style={{width: 500, height: 500 }}>
                    {
                        arr.map((value,key)=>{
                          return<p  key={key}>{value}</p>
                        })
                    }
                </Scrollbars>
            </div> 
            </div>
    )
}

export default SongDetailPage