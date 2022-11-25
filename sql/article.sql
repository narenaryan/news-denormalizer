--
-- Name: article; Type: TABLE; Schema: usa; Owner: root
--

CREATE TABLE usa.article (
    url character varying,
    title character varying NOT NULL,
    author character varying NOT NULL,
    content character varying,
    image character varying,
    description character varying,
    published_at timestamp without time zone,
    source character varying
);


ALTER TABLE usa.article OWNER TO root;

--
-- Name: article article_pkey; Type: CONSTRAINT; Schema: usa; Owner: root
--

ALTER TABLE ONLY usa.article
    ADD CONSTRAINT article_pkey PRIMARY KEY (title, author);
