/** @type {import('next').NextConfig} */
const nextConfig = {
    async rewrites() {
        return [
            {
                source: '/py/:path*',
                destination: 'http://localhost:8000/:path*',
            },
        ]
    },
};

export default nextConfig;
