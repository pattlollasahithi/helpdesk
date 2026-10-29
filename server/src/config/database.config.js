import { MongoClient } from "mongodb";

export const isMongoConfigured = () => {
    const uri = process.env.MONGODB_URI || "";

    if (!uri.trim()) {
        return false;
    }

    return !uri.includes("<db_username>") && !uri.includes("<db_password>");
};

export default async function connectDB() {
    if (!isMongoConfigured()) {
        console.log("MongoDB not configured; skipping database connection.");
        return null;
    }

    const client = new MongoClient(process.env.MONGODB_URI);
    await client.connect();
    console.log("MongoDB connected successfully.");
    return client;
}
