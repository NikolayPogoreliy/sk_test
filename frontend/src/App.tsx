import React from 'react';
import ApolloClient from 'apollo-boost';
import {ApolloProvider} from '@apollo/react-hooks';
import {UserInfo} from "./UserInfo";
import {CreateUser} from "./UserForm";

const client = new ApolloClient({
  uri: 'graphql/', // GraphQL Server
});

const App = () => (
  <ApolloProvider client={client}>
    <div style={{
      backgroundColor: '#00000008',
      display: 'flex',
      justifyContent:'center',
      alignItems:'center',
      height: '100vh',
      flexDirection: 'column',
    }}>
      <h2>Django + ReactJS + GraphQL app <span role="img" aria-label="rocket">🚀</span></h2>
      <UserInfo />
      <CreateUser />
    </div>
  </ApolloProvider>
);

export default App;
