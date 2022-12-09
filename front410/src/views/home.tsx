import { UploadOutlined, UserOutlined, VideoCameraOutlined } from '@ant-design/icons';
import { Layout, Menu } from 'antd';
import {Outlet,useNavigate} from "react-router-dom"
import React, { useState } from 'react';

const { Header, Content, Footer, Sider } = Layout;

import type { MenuProps } from 'antd';
type MenuItem = Required<MenuProps>['items'][number];

import {
    DesktopOutlined,
    FileOutlined,
    PieChartOutlined,
    TeamOutlined,
    } from '@ant-design/icons';

function getItem(
    label: React.ReactNode,
    key: React.Key,
    icon?: React.ReactNode,
    children?: MenuItem[],
    ): MenuItem {
        return {
        key,
        icon,
        children,
        label,
        } as MenuItem;
    }

const items: MenuItem[] = [
    getItem('Recommendation', "/recommendation", <TeamOutlined />),
    getItem('Lyrics Search', "/lyricsSearchArea", <PieChartOutlined />),
    getItem('Search Mood', '/sentimentSearch', <DesktopOutlined />),
    getItem('', '/LSdetail', null)
    ];




const View: React.FC = () => {
    const [collapsed, setCollapsed] = useState(false);
    const navigateTo = useNavigate();
    const menuClick = (e:{key:string}) =>{
        {/* console.log(e.key);*/}
        navigateTo(e.key)
    }
    // const navigateTo = useNavigate()
    return (
      <Layout style={{ minHeight: '100vh' }}>
        {/* 左边侧边栏 */}
        <Sider collapsible collapsed={collapsed} onCollapse={value => setCollapsed(value)}>
          <div className="logo"></div>
          <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline" items={items} onClick={menuClick} />
        </Sider>
        {/* 右边内容 */}
        <Layout className="site-layout">
          {/* 右边头部 */}
          <Header className="site-layout-background" style={{ paddingLeft: '16px' }} >

          </Header>
          {/* 右边内容部分-白色底盒子 */}
          <Content style={{ margin: '16px 16px 0', minHeight: 1500 }} className="site-layout-background">
              {/* 窗口部分 */}
              <Outlet />
          </Content>
          {/* 右边底部 */}
          <Footer style={{ textAlign: 'center', padding:0, lineHeight:"48px" }}>Music Search ©2022 Created by CS410</Footer>
        </Layout>
      </Layout>
    );
  };
// const View: React.FC = () => (
    
//   <Layout style={{ minHeight: '100vh' }}>
//     <Sider
//       breakpoint="lg"
//       collapsedWidth="0"
//       onBreakpoint={(broken) => {
//         console.log(broken);
//       }}
//       onCollapse={(collapsed, type) => {
//         console.log(collapsed, type);
//       }}
//     >
//       <div className="logo" />
//       <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline" items={items} onClick={menuClick} />
//     </Sider>

//     <Layout className="site-layout">
//       <Header className="site-layout-background" style={{ padding: 0 }} />

//       <Content style={{ margin: '24px 16px 0' }}>
//         <div className="site-layout-background" style={{ padding: 24, minHeight: 500 }}>
//           content
//         </div>
//       </Content>

//       <Footer style={{ textAlign: 'center' }}>Ant Design ©2018 Created by Ant UED</Footer>
//     </Layout>
//   </Layout>
// );

export default View;