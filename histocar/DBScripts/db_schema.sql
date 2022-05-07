SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: ar_internal_metadata; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE ar_internal_metadata (
    key character varying NOT NULL,
    value character varying,
    created_at timestamp without time zone NOT null default now(),
    updated_at timestamp without time zone NOT null default now()
);


--
-- Name: car_conditions; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE car_conditions (
    id bigint NOT NULL,
    condition_status character varying,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone NOT null default now(),
    updated_at timestamp without time zone NOT null default now()
);


--
-- Name: car_conditions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE car_conditions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: car_conditions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE car_conditions_id_seq OWNED BY car_conditions.id;


--
-- Name: car_maps; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE car_maps (
    id bigint NOT NULL,
    onlinecardealer_id integer,
    vehicle_model_id integer,
    vehicle_make_id integer,
    mapped_model_id integer,
    mapped_make_id integer,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone NOT null default now(),
    updated_at timestamp without time zone NOT null default now()
);


--
-- Name: car_maps_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE car_maps_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: car_maps_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE car_maps_id_seq OWNED BY car_maps.id;


--
-- Name: cities; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--


CREATE TABLE states (
    id bigint NOT NULL,
	state character varying,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone NOT null default now(),
    updated_at timestamp without time zone NOT null default now()
);

CREATE SEQUENCE states_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


CREATE TABLE cities (
    id bigint NOT NULL,
    state_id integer,
    city character varying,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone NOT null default now(),
    updated_at timestamp without time zone NOT null default now()
);


--
-- Name: cities_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE cities_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: cities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE cities_id_seq OWNED BY cities.id;


--
-- Name: colors; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE colors (
    id bigint NOT NULL,
    color character varying,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone NOT null default now(),
    updated_at timestamp without time zone NOT null default now()
);


--
-- Name: colors_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE colors_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: colors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE colors_id_seq OWNED BY colors.id;


--
-- Name: currencies; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE currencies (
    id bigint NOT NULL,
    currency character varying,
    currency_symbol character varying,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone NOT null default now(),
    updated_at timestamp without time zone NOT null default now()
);


--
-- Name: currencies_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE currencies_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: currencies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE currencies_id_seq OWNED BY currencies.id;


--
-- Name: histocar_lists; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE histocar_lists (
    id bigint NOT NULL,
    vehicle_model_id integer,
    vehicle_make_id integer,
    zipcode_id integer,
    onlinecardealer_id integer,
    vin_number character varying,
    price double precision,
    mileage integer,
    color_id integer,
    currency_id integer,
    carcondition_id integer,
    seller_name character varying,
    seller_address text,
    seller_telnumber character varying,
    seller_address_region character varying,
    seller_address_locality character varying,
    image_url text,
    image_local_url text,
    content_url text,
    content_local_url text,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone NOT null default now(),
    updated_at timestamp without time zone NOT null default now()
);


--
-- Name: histocar_lists_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE histocar_lists_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: histocar_lists_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE histocar_lists_id_seq OWNED BY histocar_lists.id;


--
-- Name: onlinecardealers; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE onlinecardealers (
    id bigint NOT NULL,
    dealer character varying,
    website_url text,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone NOT null default now(),
    updated_at timestamp without time zone NOT null default now()
);


--
-- Name: onlinecardealers_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE onlinecardealers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: onlinecardealers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE onlinecardealers_id_seq OWNED BY onlinecardealers.id;


--
-- Name: schema_migrations; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE schema_migrations (
    version character varying NOT NULL
);


--
-- Name: urllists; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE urllists (
    id bigint NOT NULL,
    onlinecardealer_id integer,
    vehicle_make_id integer,
    vehicle_model_id integer,
    zipcode_id character varying,
    url text,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone NOT null default now(),
    updated_at timestamp without time zone NOT null default now()
);


--
-- Name: urllists_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE urllists_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: urllists_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE urllists_id_seq OWNED BY urllists.id;


--
-- Name: vehicle_makes; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE vehicle_makes (
    id bigint NOT NULL,
    vehicle_make character varying,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone NOT null default now(),
    updated_at timestamp without time zone NOT null default now()
);


--
-- Name: vehicle_makes_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE vehicle_makes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: vehicle_makes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE vehicle_makes_id_seq OWNED BY vehicle_makes.id;


--
-- Name: vehicle_models; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE vehicle_models (
    id bigint NOT NULL,
    vehicle_make_id integer,
    model character varying,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone NOT null default now(),
    updated_at timestamp without time zone NOT null default now()
);


--
-- Name: vehicle_models_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE vehicle_models_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: vehicle_models_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE vehicle_models_id_seq OWNED BY vehicle_models.id;


--
-- Name: zipcodes; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE zipcodes (
    id bigint NOT NULL,
    zipcode character varying,
    city_id integer,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone NOT null default now(),
    updated_at timestamp without time zone NOT null default now()
);


--
-- Name: zipcodes_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE zipcodes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: zipcodes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE zipcodes_id_seq OWNED BY zipcodes.id;

ALTER SEQUENCE states_id_seq OWNED BY states.id;

--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY car_conditions ALTER COLUMN id SET DEFAULT nextval('car_conditions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY car_maps ALTER COLUMN id SET DEFAULT nextval('car_maps_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY cities ALTER COLUMN id SET DEFAULT nextval('cities_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY colors ALTER COLUMN id SET DEFAULT nextval('colors_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY currencies ALTER COLUMN id SET DEFAULT nextval('currencies_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY histocar_lists ALTER COLUMN id SET DEFAULT nextval('histocar_lists_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY onlinecardealers ALTER COLUMN id SET DEFAULT nextval('onlinecardealers_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY urllists ALTER COLUMN id SET DEFAULT nextval('urllists_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY vehicle_makes ALTER COLUMN id SET DEFAULT nextval('vehicle_makes_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY vehicle_models ALTER COLUMN id SET DEFAULT nextval('vehicle_models_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY zipcodes ALTER COLUMN id SET DEFAULT nextval('zipcodes_id_seq'::regclass);

ALTER TABLE ONLY states ALTER COLUMN id SET DEFAULT nextval('states_id_seq'::regclass);


--
-- Name: ar_internal_metadata_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY ar_internal_metadata
    ADD CONSTRAINT ar_internal_metadata_pkey PRIMARY KEY (key);


--
-- Name: car_conditions_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY car_conditions
    ADD CONSTRAINT car_conditions_pkey PRIMARY KEY (id);


--
-- Name: car_maps_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY car_maps
    ADD CONSTRAINT car_maps_pkey PRIMARY KEY (id);


--
-- Name: cities_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY cities
    ADD CONSTRAINT cities_pkey PRIMARY KEY (id);


--
-- Name: colors_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY colors
    ADD CONSTRAINT colors_pkey PRIMARY KEY (id);


--
-- Name: currencies_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY currencies
    ADD CONSTRAINT currencies_pkey PRIMARY KEY (id);


--
-- Name: histocar_lists_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY histocar_lists
    ADD CONSTRAINT histocar_lists_pkey PRIMARY KEY (id);


--
-- Name: onlinecardealers_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY onlinecardealers
    ADD CONSTRAINT onlinecardealers_pkey PRIMARY KEY (id);


--
-- Name: schema_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY schema_migrations
    ADD CONSTRAINT schema_migrations_pkey PRIMARY KEY (version);


--
-- Name: urllists_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY urllists
    ADD CONSTRAINT urllists_pkey PRIMARY KEY (id);


--
-- Name: vehicle_makes_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY vehicle_makes
    ADD CONSTRAINT vehicle_makes_pkey PRIMARY KEY (id);


--
-- Name: vehicle_models_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY vehicle_models
    ADD CONSTRAINT vehicle_models_pkey PRIMARY KEY (id);


--
-- Name: zipcodes_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY zipcodes
    ADD CONSTRAINT zipcodes_pkey PRIMARY KEY (id);


ALTER TABLE ONLY states
    ADD CONSTRAINT states_pkey PRIMARY KEY (id);

	
--
-- PostgreSQL database dump complete
--

SET search_path TO "$user",public;

INSERT INTO "schema_migrations" (version) VALUES
('20181117042146'),
('20181117042307'),
('20181117042345'),
('20181117042411'),
('20181117042558'),
('20181117042838'),
('20181117042917'),
('20181117042951'),
('20181117043026'),
('20181117043107'),
('20181117043235'),
('20181117043335');