import {useMutation} from 'react-apollo';
import {gql} from 'apollo-boost';

const CREATE_USER = gql`
  mutation createUser ($firstName: String!, $lastName: String!){
    createUser (firstName: $firstName, lastName: $lastName){
      id
      firstName
      lastName
  }
}
`;

export function CreateUser() {
    let firstName: { value: string };
    let lastName: { value: string };
    const [createUser] = useMutation(CREATE_USER);
    return (
        <div>
            <form
                onSubmit={e => {
                    e.preventDefault();
                    createUser({
                        variables: {
                            firstName: firstName.value,
                            lastName: lastName.value
                        }
                    }).then(() => {
                        firstName.value = '';
                        lastName.value = '';
                        window.location.reload();
                    });
                }}
                style={{marginTop: '2em', marginBottom: '2em'}}
            >
                <label>First Name: </label>
                <input
                    ref={node => {
                        // @ts-ignore
                        firstName = node;
                    }}
                    style={{marginRight: '1em'}}
                />
                <label>Last Name: </label>
                <input
                    ref={node => {
                        // @ts-ignore
                        lastName = node;
                    }}
                    style={{marginRight: '1em'}}
                />

                <button type="submit" style={{cursor: 'pointer'}}>Add a User</button>
            </form>
        </div>
    );
}