import { getUser } from "../utils/Helper";

const Home = () =>
{
    return <h1>Hello, {getUser().username}</h1>;
}

export default Home;