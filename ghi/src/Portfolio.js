import { Box, Heading, Text, Link, UnorderedList, ListItem, Input, Button, VStack, HStack } from '@chakra-ui/react';

const Portfolio = () => {
  return (
    <Box textAlign="center">
      <Box as="header" p="20px">
        <Heading as="h1" color="blue.500" fontSize="2.5rem">Your Name</Heading>
        <Text fontSize="1.2rem" color="blue.300">Expert in Web Development and Design</Text>
      </Box>

      <Box as="nav">
        <UnorderedList styleType="none" m="0" p="0">
          <ListItem display="inline" mx="15px">
            <Link href="#introduction" color="blue.200" fontWeight="bold">Introduction</Link>
          </ListItem>
          <ListItem display="inline" mx="15px">
            <Link href="#projects" color="blue.200" fontWeight="bold">Projects</Link>
          </ListItem>
          <ListItem display="inline" mx="15px">
            <Link href="#contact" color="blue.200" fontWeight="bold">Contact</Link>
          </ListItem>
        </UnorderedList>
      </Box>

      <VStack spacing="40px" my="40px">
        <Box as="section" id="introduction">
          <Heading as="h2">About Me</Heading>
          <Text>Brief description about your skills and experience.</Text>
        </Box>

        <Box as="section" id="projects">
          <Heading as="h2">Projects</Heading>
          {/* Repeat this block for each project */}
          <VStack>
            <Heading as="h3">Project Title</Heading>
            <Text>Short description of the project.</Text>
            <HStack>
              <Link href="live-link" p="10px 15px" bg="blue.500" borderRadius="5px" color="white" _hover={{ bg: 'blue.300' }}>Live Demo</Link>
              <Link href="repo-link" p="10px 15px" bg="blue.500" borderRadius="5px" color="white" _hover={{ bg: 'blue.300' }}>Repository</Link>
            </HStack>
          </VStack>
        </Box>

        <Box as="section" id="contact">
          <Heading as="h2">Contact</Heading>
          <form action="submit-form-link">
            <Input placeholder="Your email" type="email" mb="20px" />
            <Button type="submit" value="Subscribe">Subscribe</Button>
          </form>
        </Box>
      </VStack>

      <Box as="footer" fontSize="0.8rem" color="gray.400" py="20px">
        <Text>© 2024 Your Name. All rights reserved.</Text>
      </Box>
    </Box>
  );
};

export default Portfolio;
